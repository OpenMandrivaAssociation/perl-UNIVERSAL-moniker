%define upstream_name    UNIVERSAL-moniker
%define upstream_version 0.08

%if %{_use_internal_dependency_generator}
%define __noautoprov 'perl\\(UNIVERSAL\\)'
%else
%define _provides_exceptions perl(UNIVERSAL)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	UNIVERSAL::moniker
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/UNIVERSAL/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Class names in Perl often don't sound great when spoken, or look
good when written in prose. For this reason, we tend to say things
like "customer" or "basket" when we are referring to 
My::Site::User::Customer or My::Site::Shop::Basket. We thought it
would be nice if our classes knew what we would prefer to call
them. This module will add a moniker (and plural_moniker) method
to UNIVERSAL, and so to every class or module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/UNIVERSAL/moniker.pm
%{_mandir}/*/*

%changelog
* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 401959
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.08-6mdv2009.0
+ Revision: 242114
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.08-4mdv2008.0
+ Revision: 23627
- rebuild


* Mon May 15 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.08-3mdk
- Don't provide perl(UNIVERSAL)

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.08-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.08-1mdk
- initial Mandriva package

