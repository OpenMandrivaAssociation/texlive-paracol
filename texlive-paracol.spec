%global tl_name paracol
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.37
Release:	%{tl_revision}.1
Summary:	Multiple columns with texts in parallel
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/paracol
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/paracol.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/paracol.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/paracol.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides yet another multi-column typesetting mechanism by
which you produce multi-column (e.g., bilingual) document switching and
synchronizing each corresponding part in "parallel".

