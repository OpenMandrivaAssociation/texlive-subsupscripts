%global tl_name subsupscripts
%global tl_revision 16080

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A range of sub- and superscript commands
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/subsupscripts
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subsupscripts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subsupscripts.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a comprehensive and flexible set of commands for
combinations of left and right sub- and superscripts.

