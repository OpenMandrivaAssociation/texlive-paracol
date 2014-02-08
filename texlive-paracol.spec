# revision 26474
# category Package
# catalog-ctan /macros/latex/contrib/paracol
# catalog-date 2012-05-17 13:04:31 +0200
# catalog-license lppl
# catalog-version 1.10
Name:		texlive-paracol
Version:	1.10
Release:	2
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
%doc %{_texmfdistdir}/source/latex/paracol/impl.dtx
%doc %{_texmfdistdir}/source/latex/paracol/man.dtx
%doc %{_texmfdistdir}/source/latex/paracol/paracol.dtx
%doc %{_texmfdistdir}/source/latex/paracol/paracol.ins
%doc %{_texmfdistdir}/source/latex/paracol/ref.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.10-1
+ Revision: 812724
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.00-2
+ Revision: 754641
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.00-1
+ Revision: 719189
- texlive-paracol
- texlive-paracol
- texlive-paracol
- texlive-paracol

