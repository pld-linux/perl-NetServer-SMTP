%include	/usr/lib/rpm/macros.perl
Summary:	NetServer-SMTP perl module
Summary(pl):	Modu³ perla NetServer-SMTP
Name:		perl-NetServer-SMTP
Version:	0.01
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/NetServer/NetServer-SMTP-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-libnet
BuildRequires:	perl-FreezeThaw
BuildRequires:	perl-File-Flock
BuildRequires:	perl-Time-modules
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetServer-SMTP - basic SMTP server class for Perl.

%description -l pl
NetServer-SMTP - podstawowa klasa serwera SMTP.

%prep
%setup -q -n NetServer-SMTP-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/NetServer/SMTP
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/NetServer/SMTP.pm
%{perl_sitearch}/auto/NetServer/SMTP

%{_mandir}/man3/*

%{_prefix}/src/examples/%{name}-%{version}
