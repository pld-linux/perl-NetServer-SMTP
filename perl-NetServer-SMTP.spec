%include	/usr/lib/rpm/macros.perl
%define	pdir	NetServer
%define	pnam	SMTP
Summary:	NetServer::SMTP perl module
Summary(pl):	Modu³ perla NetServer::SMTP
Name:		perl-NetServer-SMTP
Version:	0.01
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildRequires:	perl-libnet
BuildRequires:	perl-FreezeThaw
BuildRequires:	perl-File-Flock
BuildRequires:	perl-Time-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetServer::SMTP - basic SMTP server class for Perl.

%description -l pl
NetServer::SMTP - podstawowa klasa serwera SMTP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/NetServer/SMTP.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
