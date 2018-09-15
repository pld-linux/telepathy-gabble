Summary:	A Telepathy connection manager for Jabber/XMPP
Summary(pl.UTF-8):	Zarządca połączeń Telepathy dla Jabbera/XMPP
Name:		telepathy-gabble
Version:	0.18.4
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://telepathy.freedesktop.org/releases/telepathy-gabble/%{name}-%{version}.tar.gz
# Source0-md5:	64334f42b1822dbc22b823f22f9e968f
URL:		https://telepathy.freedesktop.org/wiki/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.11
BuildRequires:	cyrus-sasl-devel
BuildRequires:	dbus-devel >= 1.1.0
BuildRequires:	dbus-glib-devel >= 0.82
BuildRequires:	glib2-devel >= 1:2.44
BuildRequires:	libnice-devel >= 0.0.11
BuildRequires:	libsoup-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-progs
BuildRequires:	openssl-devel >= 0.9.8g
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
BuildRequires:	sqlite3-devel
BuildRequires:	telepathy-glib-devel >= 0.19.9
BuildRequires:	which
Requires:	ca-certificates
Requires:	dbus >= 1.1.0
Requires:	dbus-glib >= 0.82
Requires:	glib2 >= 1:2.44
Requires:	libnice >= 0.0.11
Requires:	telepathy-glib >= 0.19.9
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
	--disable-static \
	--with-ca-certificates=%{_sysconfdir}/certs/ca-certificates.crt \
	--with-tls=openssl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/telepathy/gabble-0/plugins/*.la
# private libraries, API not exported
%{__rm} $RPM_BUILD_ROOT%{_libdir}/telepathy/gabble-0/lib/lib{gabble-plugins,wocky}.{so,la}
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc/telepathy-gabble

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README docs/*.html
%attr(755,root,root) %{_bindir}/telepathy-gabble-xmpp-console
%attr(755,root,root) %{_libdir}/telepathy-gabble
%dir %{_libdir}/telepathy
%dir %{_libdir}/telepathy/gabble-0
%dir %{_libdir}/telepathy/gabble-0/lib
%attr(755,root,root) %{_libdir}/telepathy/gabble-0/lib/libgabble-plugins-%{version}.so
%attr(755,root,root) %{_libdir}/telepathy/gabble-0/lib/libwocky-telepathy-gabble-%{version}.so
%dir %{_libdir}/telepathy/gabble-0/plugins
%attr(755,root,root) %{_libdir}/telepathy/gabble-0/plugins/libconsole.so
%attr(755,root,root) %{_libdir}/telepathy/gabble-0/plugins/libgateways.so
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.gabble.service
%{_datadir}/telepathy/managers/gabble.manager
%{_mandir}/man8/telepathy-gabble.8*
