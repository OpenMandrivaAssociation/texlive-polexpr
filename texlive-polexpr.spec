Name:		texlive-polexpr
Version:	63337
Release:	2
Summary:	A parser for polynomial expressions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/polexpr
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polexpr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polexpr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a parser \poldef of algebraic polynomial
expressions. As it is based on xintexpr, the coefficients are
allowed to be arbitrary rational numbers. Once defined, a
polynomial is usable by its name either as a numerical function
in \xintexpr/\xinteval, or for additional polynomial
definitions, or as argument to the package macros. The
localization of real roots to arbitrary precision as well as
the determination of all rational roots is implemented via such
macros. Since release 0.8, polexpr extends the xintexpr syntax
to recognize polynomials as a new variable type (and not only
as functions). Functionality which previously was implemented
via macros such as the computation of a greatest common divisor
is now available directly in \xintexpr, \xinteval or \poldef
via infix or functional syntax.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/polexpr
%doc %{_texmfdistdir}/doc/generic/polexpr

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
