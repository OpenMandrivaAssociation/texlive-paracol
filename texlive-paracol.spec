# revision 24426
# category Package
# catalog-ctan /macros/latex/contrib/paracol
# catalog-date 2011-10-27 18:19:57 +0200
# catalog-license lppl
# catalog-version 1.00
Name:		texlive-paracol
Version:	1.00
Release:	1
Summary:	Multiple columns with texts "in parallel"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/paracol
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paracol.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paracol.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paracol.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides yet another multi-column typesetting
mechanism by which you produce multi-column (e.g., bilingual)
document switching and sychronizing each corresponding part in
"parallel".

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
%{_texmfdistdir}/tex/latex/paracol/paracol.sty
%doc %{_texmfdistdir}/doc/latex/paracol/README
%doc %{_texmfdistdir}/doc/latex/paracol/paracol-man.pdf
%doc %{_texmfdistdir}/doc/latex/paracol/paracol-man.tex
#- source
%doc %{_texmfdistdir}/source/latex/paracol/impl.dtx
%doc %{_texmfdistdir}/source/latex/paracol/man.dtx
%doc %{_texmfdistdir}/source/latex/paracol/paracol.dtx
%doc %{_texmfdistdir}/source/latex/paracol/paracol.ins
%doc %{_texmfdistdir}/source/latex/paracol/ref.dtx
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
