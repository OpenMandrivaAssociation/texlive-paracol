# revision 32099
# category Package
# catalog-ctan /macros/latex/contrib/paracol
# catalog-date 2013-11-08 18:09:20 +0100
# catalog-license lppl
# catalog-version 1.31
Name:		texlive-paracol
Version:	1.31
Release:	3
Summary:	Multiple columns with texts "in parallel"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/paracol
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paracol.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paracol.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paracol.source.tar.xz
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
%{_texmfdistdir}/tex/latex/paracol/paracol.sty
%doc %{_texmfdistdir}/doc/latex/paracol/README
%doc %{_texmfdistdir}/doc/latex/paracol/paracol-man.pdf
%doc %{_texmfdistdir}/doc/latex/paracol/paracol-man.tex
#- source
%doc %{_texmfdistdir}/source/latex/paracol/bgpaint.dtx
%doc %{_texmfdistdir}/source/latex/paracol/impl.dtx
%doc %{_texmfdistdir}/source/latex/paracol/ltfloat.dtx
%doc %{_texmfdistdir}/source/latex/paracol/man.dtx
%doc %{_texmfdistdir}/source/latex/paracol/paracol.dtx
%doc %{_texmfdistdir}/source/latex/paracol/paracol.ins
%doc %{_texmfdistdir}/source/latex/paracol/probs.dtx
%doc %{_texmfdistdir}/source/latex/paracol/pwfnote.dtx
%doc %{_texmfdistdir}/source/latex/paracol/ref.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
