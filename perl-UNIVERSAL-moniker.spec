%define upstream_name    UNIVERSAL-moniker
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	UNIVERSAL::moniker
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/UNIVERSAL/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%define _provides_exceptions perl(UNIVERSAL)

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/UNIVERSAL/moniker.pm
%{_mandir}/*/*
