Summary:	unZOO - extract, test and view ZOO archives.
Summary(pl):	unZOO - rozpakowuje, testuje i przegl±da archiwa ZOO.
Name:		unzoo
Version:	4.4
Release:	1
Copyright:	Public Domain
Group:		Utilities/Archiving
Group(pl):	Narzêdzia/Archiwizacja
URL:		ftp://ftp.math.rwth-aachen.de/pub/gap/gap4/util/unzoo.c
Source:		unzoo.c.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unzoo utility is a Public Domain program, distributed with source code and
developed for extracting, testing and viewing the contents of archives created
with the ZOO archiver.

%description -l pl
UnACE jest programem freeware, rozpowszechnianym wraz z kodem ¼ród³owym, 
przeznaczonym do rozpakowywania, testowania oraz przegl±dania zawarto¶ci
archiwów stworzonych przez program ZOO.

%prep
%setup -q -c -T
gzip -dc %{SOURCE0} > unzoo.c

%build
gcc $RPM_OPT_FLAGS -DSYS_IS_UNIX unzoo.c -o unzoo

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install -s unzoo $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/unzoo
