Name:		perl-XString
Version:	0.005
Release:	4%{?dist}
Summary:	Isolated String helpers from B
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/XString
Source0:	https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/XString-%{version}.tar.gz
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:	perl(:VERSION) >= 5.10.0
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# Test Suite
BuildRequires:	perl(B)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More) >= 0.88
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
# Runtime
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:	perl(XSLoader)

%description
XString provides the B string helpers in one isolated package. Right now only
cstring and perlstring are available.

%prep
%setup -q -n XString-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/XString.pm
%{perl_vendorarch}/auto/XString/
%{_mandir}/man3/XString.3*

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 0.005-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.005-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 20 2020 Paul Howarth <paul@city-fan.org> - 0.005-1
- Update to 0.005
  - Fix cstring for Perl 5.32 (GH#6, GH#7)
  - Remove unneeded module dependencies (GH#2)
  - Add compatibility with Perl 5.8 (GH#9)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.002-4
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Paul Howarth <paul@city-fan.org> - 0.002-2
- Incorporate feedback from package review (#1776513)
  - BR: findutils
  - BR: perl(CPAN::Meta::Prereqs)
  - Need perl(ExtUtils::MakeMaker) >= 6.76
  - Add reference to upstream ticket about unnecessary build requirements
    https://github.com/atoomic/XString/issues/2
  - Add run-time dependency on perl(XSLoader)

* Mon Nov 25 2019 Paul Howarth <paul@city-fan.org> - 0.002-1
- Initial RPM version
