# revision 16080
# category Package
# catalog-ctan /macros/latex/contrib/subsupscripts
# catalog-date 2009-11-20 12:24:11 +0100
# catalog-license noinfo
# catalog-version 1.0
Name:		texlive-subsupscripts
Version:	1.0
Release:	3
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

%description
The package provides a comprehensive and flexible set of
commands for combinations of left and right sub- and
superscripts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/subsupscripts/subsupscripts.sty
%doc %{_texmfdistdir}/doc/latex/subsupscripts/README
%doc %{_texmfdistdir}/doc/latex/subsupscripts/SubSupScripts.pdf
%doc %{_texmfdistdir}/doc/latex/subsupscripts/SubSupScripts.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 756334
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719608
- texlive-subsupscripts
- texlive-subsupscripts
- texlive-subsupscripts
- texlive-subsupscripts

