#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	CDCollect is a simple CD catalog for GNOME
Summary(pl.UTF-8):	CDCollect jest prostym programem do katalogowania płyt CD napisanym dla GNOME	
Name:		cdcollect
Version:	0.6.0
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	33f71604b9dfb84497b4bc2fce69e89b
URL:		http://cdcollect.sourceforge.net/

#BuildRequires:	-
#BuildRequires:	autoconf
#BuildRequires:	automake
#BuildRequires:	intltool
#BuildRequires:	libtool
#Requires(postun):	-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires:	-
#Provides:	-
#Provides:	group(foo)
#Provides:	user(foo)
#Obsoletes:	-
#Conflicts:	-
#BuildArch:	noarch
#ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CDCollect is a CD/DVD catalog application for gnome 2.16. Its functionality is
similar to the old gtktalog application for gnome 1.4.

It's goal is to be able to catalog your entire CD collection allowing for
searches of your CD/DVD files with a clean and simple interface.

%description -l pl.UTF-8
CDCollect jest programem do katalogowania płyt CD/DVD dla GNOME. Jego
funkcjonalność jest podobna do starego gtkatalog

Możesz w prosty sposób katalogować zawartość swoich płyt CD oraz przeszukiwać
bazę za pomocą łatwego w użyciu interfejsu użytkownika


%prep
%setup -q
#%setup -q -c -T
#%setup -q -n %{name}
#%setup -q -n %{name}-%{version}.orig -a 1
#%patch0 -p1

# undos the source
#find '(' -name '*.php' -o -name '*.inc' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

# remove CVS control files
#find -name CVS -print0 | xargs -0 rm -rf

# you'll need this if you cp -a complete dir in source
# cleanup backups after patching
find . '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__intltoolize}
#%%{__gettextize}
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
#cp -f /usr/share/automake/config.sub .
%configure
%{__make}

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
#rm -rf $RPM_BUILD_ROOT

%pre

%post
%gconf_schema_install %{name}.schemas

%preun
%gconf_schema_install %{name}.schemas

%postun


%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/*
%{_datadir}/locale/*/LC_MESSAGES/*
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_pixmapsdir}/*
