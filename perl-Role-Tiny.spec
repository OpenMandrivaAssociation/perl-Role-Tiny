%define	upstream_name    Role-Tiny

Name:		perl-%{upstream_name}
Version:	2.002004
Release:	1

Summary:	Roles for Perl
License:	Artistic 2.0
Group:		Development/Perl
Url:		https://metacpan.org/pod/Role::Tiny
Source0:	http://search.cpan.org/CPAN/authors/id/H/HA/HAARG/%{upstream_name}-%{version}.tar.gz

BuildRequires:  perl-devel
BuildRequires:	perl(namespace::clean)
BuildRequires:	perl(Module::Build)

BuildArch:	noarch


%description
Roles for Perl

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
perl Makefile.PL installdirs=vendor destdir=%{buildroot}
%make_build

%install
%make_install

%files
%doc Changes 
%{perl_vendorlib}/Role
%{_mandir}/*/*
