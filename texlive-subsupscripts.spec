Name:		texlive-subsupscripts
Version:	16080
Release:	1
Summary:	A range of sub- and superscript commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/subsupscripts
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subsupscripts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subsupscripts.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
