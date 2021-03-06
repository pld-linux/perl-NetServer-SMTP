%define		pdir	NetServer
%define		pnam	SMTP
Summary:	NetServer::SMTP perl module
Summary(pl.UTF-8):	Moduł perla NetServer::SMTP
Name:		perl-NetServer-SMTP
Version:	0.01
Release:	12
# same as perl (but sending unsolicited commercial mail require a fee)
License:	GPL v1+ or Artistic (with one restriction, see LICENSE)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	46f345dfc3e7022c3c0f8bdc94a9a700
URL:		http://search.cpan.org/dist/NetServer-SMTP/
BuildRequires:	perl-File-Flock
BuildRequires:	perl-FreezeThaw
BuildRequires:	perl-Time-modules
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libnet
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetServer::SMTP - basic SMTP server class for Perl.

%description -l pl.UTF-8
NetServer::SMTP - podstawowa klasa serwera SMTP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README LICENSE
%{perl_vendorlib}/NetServer/SMTP.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
