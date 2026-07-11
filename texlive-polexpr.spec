%global tl_name polexpr
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.8.7a
Release:	%{tl_revision}.1
Summary:	A parser for polynomial expressions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/polexpr
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/polexpr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/polexpr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a parser \poldef of algebraic polynomial
expressions. As it is based on xintexpr, the coefficients are allowed to
be arbitrary rational numbers. Once defined, a polynomial is usable by
its name either as a numerical function in \xintexpr/\xinteval, or for
additional polynomial definitions, or as argument to the package macros.
The localization of real roots to arbitrary precision as well as the
determination of all rational roots is implemented via such macros.
Since release 0.8, polexpr extends the xintexpr syntax to recognize
polynomials as a new variable type (and not only as functions).
Functionality which previously was implemented via macros such as the
computation of a greatest common divisor is now available directly in
\xintexpr, \xinteval or \poldef via infix or functional syntax.

