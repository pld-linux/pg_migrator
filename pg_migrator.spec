Summary:	In-place data upgrade utility for PostgreSQL
Name:		pg_migrator
Version:	8.4.19
Release:	1
License:	BSD
Group:		Applications/Databases
Source0:	http://pgfoundry.org/frs/download.php/2695/%{name}-%{version}.tgz
# Source0-md5:	b71a514c75403c522093e1e511ffb278
URL:		http://pgfoundry.org/projects/pg-migrator
BuildRequires:	postgresql-devel >= 8.4
Requires:	postgresql >= 8.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pg_migrator performs an in-place upgrade of existing data when
upgrading from an old release of PostgreSQL to a new release. Use
pg_migrator to avoid the typical (and painful) pg_dump/reload cycle
required by many upgrades.

%prep
%setup -q

%build
%{__make} \
	USE_PGXS=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_docdir}/%{name}-%{version},%{_libdir}}

install src/pg_migrator $RPM_BUILD_ROOT%{_bindir}
install func/pg_migrator*.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DEVELOPERS IMPLEMENTATION INSTALL LICENSE README TODO
%attr(755,root,root) %{_bindir}/pg_migrator
%attr(755,root,root) %{_libdir}/pg_migrator*.so
