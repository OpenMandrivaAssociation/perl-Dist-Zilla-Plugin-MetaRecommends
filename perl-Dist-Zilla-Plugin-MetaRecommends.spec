%define upstream_name    Dist-Zilla-Plugin-MetaRecommends
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Provide optional prereqs in meta file
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla::Role::MetaProvider)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This plugin adds a 'recommends' section to the distribution's metadata to
define any optional prereqs.

This module is just a copy of the MetaResources plugin version 1.092680
with a few minor tweaks.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

