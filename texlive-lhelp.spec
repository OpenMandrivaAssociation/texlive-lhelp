# revision 23638
# category Package
# catalog-ctan /macros/latex/contrib/lhelp
# catalog-date 2007-01-08 22:21:56 +0100
# catalog-license gpl
# catalog-version 2.0
Name:		texlive-lhelp
Version:	2.0
Release:	1
Summary:	Miscellaneous helper packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lhelp
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lhelp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lhelp.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lhelp.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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
%{_texmfdistdir}/tex/latex/lhelp/lhelp.sty
%doc %{_texmfdistdir}/doc/latex/lhelp/Makefile
%doc %{_texmfdistdir}/doc/latex/lhelp/lhelp.pdf
#- source
%doc %{_texmfdistdir}/source/latex/lhelp/lhelp.drv
%doc %{_texmfdistdir}/source/latex/lhelp/lhelp.dtx
%doc %{_texmfdistdir}/source/latex/lhelp/lhelp.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
