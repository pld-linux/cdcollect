Summary:	CDCollect - a simple CD catalog for GNOME
Summary(hu.UTF-8):	CDCollect - egy egyszerű CD katalogizáló GNOME-ra
Summary(pl.UTF-8):	CDCollect - prosty programem do katalogowania płyt CD napisany dla GNOME
Name:		cdcollect
Version:	0.6.0
Release:	0.3
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/cdcollect/%{name}-%{version}.tar.bz2
# Source0-md5:	33f71604b9dfb84497b4bc2fce69e89b
Source1:	%{name}-faq.txt
URL:		http://cdcollect.sourceforge.net/
BuildRequires:	dotnet-gnome-sharp-devel >= 2.8.0
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.8.0
BuildRequires:	mono-csharp >= 1.1.17
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	sqlite3-devel >= 3.3
Requires(post,preun):	GConf2
Requires:	dotnet-gnome-sharp >= 2.8.0
Requires:	dotnet-gtk-sharp2 >= 2.8.0
Requires:	mono >= 1.1.17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CDCollect is a CD/DVD catalog application for GNOME 2. Its
functionality is similar to the old gtktalog application for GNOME
1.4.

Its goal is to be able to catalog your entire CD collection allowing
for searches of your CD/DVD files with a clean and simple interface.

%description -l hu.UTF-8
CDCollect egy CD/DVD katalogizáló alkalmazás GNOME2-re. A céljai
hasonlóak a régebbi gtktalog-hoz, amely még GNOME 1.4-hez készült.

A célja, hogy az egész CD kollekciódból egy kereshető adatbázist
készítsen, egy egy tiszta és egyszerű felületen.

%description -l pl.UTF-8
CDCollect jest programem do katalogowania płyt CD/DVD dla GNOME 2.
Jego funkcjonalność jest podobna do starego programu gtkatalog dla
GNOME 1.4.

Program pozwala w prosty sposób katalogować zawartość płyt CD oraz
przeszukiwać bazę za pomocą łatwego w użyciu interfejsu użytkownika.

%prep
%setup -q
%{__cp} %{SOURCE1} FAQ

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install %{name}.schemas

%preun
%gconf_schema_uninstall %{name}.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_desktopdir}/*
%{_pixmapsdir}/*
