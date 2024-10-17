%define	upstream_name    Role-Tiny
%define upstream_version 2.002004

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Roles for Perl
License:	Artistic 2.0
Group:		Development/Perl
Url:		https://metacpan.org/pod/Role::Tiny
Source0:	http://search.cpan.org/CPAN/authors/id/H/HA/HAARG/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl-devel
BuildRequires:	perl(namespace::clean)
BuildRequires:	perl(Module::Build)

BuildArch:	noarch


%description
Roles for Perl

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL installdirs=vendor destdir=%{buildroot}
%make

%install
%makeinstall_std

%files
%doc Changes 
%{perl_vendorlib}/Role
%{_mandir}/*/*
