%include	/usr/lib/rpm/macros.perl
Summary:	NetServer-SMTP perl module
Summary(pl):	Modu� perla NetServer-SMTP
Name:		perl-NetServer-SMTP
Version:	0.01
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/NetServer/NetServer-SMTP-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-libnet
BuildRequires:	perl-FreezeThaw
BuildRequires:	perl-File-Flock
BuildRequires:	perl-Time-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetServer-SMTP - basic SMTP server class for Perl.

%description -l pl
NetServer-SMTP - podstawowa klasa serwera SMTP.

%prep
%setup -q -n NetServer-SMTP-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/NetServer/SMTP.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
