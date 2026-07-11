%global tl_name lhelp
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Miscellaneous helper packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lhelp
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lhelp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lhelp.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lhelp.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package defines macros which are useful for many documents. It is a
large collection of simple 'little helpers' which do not really warrant
a separate package on their own. Included are, among other things,
definitions of common units with preceding thinspaces, framed boxes
where both width and height can be specified, starting new odd or even
pages, draft markers, notes, conditional includes, including EPS files,
and versions of enumerate and itemize which allow the horizontal and
vertical spacing to be changed.

