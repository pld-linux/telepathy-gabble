Summary:	A Telepathy connection manager for Jabber/XMPP
Summary(pl.UTF-8):	Zarządca połączeń Telepathy dla Jabbera/XMPP
Name:		telepathy-gabble
Version:	0.7.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-gabble/%{name}-%{version}.tar.gz
# Source0-md5:	8a54160c9b081dbe2751abca89580619
URL:		http://telepathy.freedesktop.org/wiki/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.72
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	loudmouth-devel >= 1.1.1
BuildRequires:	pkgconfig
BuildRequires:	telepathy-glib-devel >= 0.5.14
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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/telepathy-gabble
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.gabble.service
%{_datadir}/telepathy/managers/gabble.manager
%{_mandir}/man8/*
