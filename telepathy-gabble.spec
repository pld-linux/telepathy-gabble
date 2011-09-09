Summary:	A Telepathy connection manager for Jabber/XMPP
Summary(pl.UTF-8):	Zarządca połączeń Telepathy dla Jabbera/XMPP
Name:		telepathy-gabble
# NOTE: 0.11.x is development branch
Version:	0.10.5
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-gabble/%{name}-%{version}.tar.gz
# Source0-md5:	6d3e07354fb6d3ea5f8375e7cf776a27
URL:		http://telepathy.freedesktop.org/wiki/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.11
BuildRequires:	dbus-devel >= 1.1.0
BuildRequires:	dbus-glib-devel >= 0.82
BuildRequires:	glib2-devel >= 1:2.24.0
BuildRequires:	gnutls-devel >= 2.8.2
BuildRequires:	libnice-devel >= 0.0.11
BuildRequires:	libsoup-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	telepathy-glib-devel >= 0.12.0
BuildRequires:	which
BuildRequires:	sqlite3-devel
Requires:	ca-certificates
Requires:	dbus >= 1.1.0
Requires:	dbus-glib >= 0.82
Requires:	telepathy-glib >= 0.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A connection manager to connect Telepathy to Jabber/XMPP.

%description -l pl.UTF-8
Zarządca połączeń pozwalający połączyć się Telepathy z Jabberem/XMPP.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-ca-certificates=%{_sysconfdir}/certs/ca-certificates.crt
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/telepathy/gabble-0/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc/telepathy-gabble

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/telepathy-gabble
%dir %{_libdir}/telepathy
%dir %{_libdir}/telepathy/gabble-0
%attr(755,root,root) %{_libdir}/telepathy/gabble-0/*.so
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.gabble.service
%{_datadir}/telepathy/managers/gabble.manager
%{_mandir}/man8/*.8*
