%define real_name UNIVERSAL-moniker

Summary:	UNIVERSAL::moniker
Name:		perl-%{real_name}
Version:	0.08
Release: %mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/UNIVERSAL/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%setup -q -n %{real_name}-%{version} 

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

