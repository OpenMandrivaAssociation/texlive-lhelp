Name:		texlive-lhelp
Version:	23638
Release:	2
Summary:	Miscellaneous helper packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lhelp
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lhelp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lhelp.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lhelp.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package defines macros which are useful for many
documents. It is a large collection of simple 'little helpers'
which do not really warrant a separate package on their own.
Included are, among other things, definitions of common units
with preceeding thinspaces, framed boxes where both width and
height can be specified, starting new odd or even pages, draft
markers, notes, conditional includes, including EPS files, and
versions of enumerate and itemize which allow the horizontal
and vertical spacing to be changed.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lhelp/lhelp.sty
%doc %{_texmfdistdir}/doc/latex/lhelp/Makefile
%doc %{_texmfdistdir}/doc/latex/lhelp/lhelp.pdf
#- source
%doc %{_texmfdistdir}/source/latex/lhelp/lhelp.drv
%doc %{_texmfdistdir}/source/latex/lhelp/lhelp.dtx
%doc %{_texmfdistdir}/source/latex/lhelp/lhelp.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
