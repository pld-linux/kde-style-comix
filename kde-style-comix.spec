
%define         _name	comix

Summary:	KDE style - %{_name}
Summary(pl):	Styl do KDE - %{_name}
Name:		kde-style-%{_name}
Version:	0.1.3
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/16028-%{_name}-%{version}.tar.bz2
# Source0-md5:	a4ee90dd8daae73da829a0bf53c8ac24
URL:		http://www.kde-look.org/content/show.php?content=16028
BuildRequires:	autoconf
BuildRequires:	unsermake
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} is a cartoon like style with rounded user interface elements.

%description -l pl
%{_name} to kreskówkowy styl z zaokr±glonymi elementami interfejsu
u¿ytkownika.

%prep
%setup -q -n %{_name}-%{version}

%build
cp -f %{_datadir}/automake/config.sub admin
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f Makefile.cvs

%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/kstyle_*.la
%attr(755,root,root) %{_libdir}/kde3/kstyle_*.so
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_libdir}/kde3/plugins/styles/*.la
%{_datadir}/apps/kstyle/themes/*.themerc
