Name:		texlive-tikz-opm
Version:	32769
Release:	2
Summary:	Typeset OPM diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-opm
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-opm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-opm.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Typeset OPM (Object-Process Methodology) diagrams using LaTeX
and pgf/TikZ.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tikz-opm/tikz-opm.sty
%doc %{_texmfdistdir}/doc/latex/tikz-opm/README
%doc %{_texmfdistdir}/doc/latex/tikz-opm/tikz-opm.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
