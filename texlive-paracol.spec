Name:		texlive-paracol
Version:	49560
Release:	2
Summary:	Multiple columns with texts "in parallel"
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/paracol
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paracol.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paracol.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paracol.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides yet another multi-column typesetting
mechanism by which you produce multi-column (e.g., bilingual)
document switching and sychronizing each corresponding part in
"parallel".

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/paracol
%doc %{_texmfdistdir}/doc/latex/paracol
#- source
%doc %{_texmfdistdir}/source/latex/paracol

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
