# revision 16080
# category Package
# catalog-ctan /macros/latex/contrib/subsupscripts
# catalog-date 2009-11-20 12:24:11 +0100
# catalog-license noinfo
# catalog-version 1.0
Name:		texlive-subsupscripts
Version:	1.0
Release:	1
Summary:	A range of sub- and superscript commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/subsupscripts
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subsupscripts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subsupscripts.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides a comprehensive and flexible set of
commands for combinations of left and right sub- and
superscripts.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/subsupscripts/subsupscripts.sty
%doc %{_texmfdistdir}/doc/latex/subsupscripts/README
%doc %{_texmfdistdir}/doc/latex/subsupscripts/SubSupScripts.pdf
%doc %{_texmfdistdir}/doc/latex/subsupscripts/SubSupScripts.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
