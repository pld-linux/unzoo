Summary:	unZOO - extract, test and view ZOO archives
Summary(pl.UTF-8):	unZOO - rozpakowywanie, testowanie i przeglądanie archiwów ZOO
Name:		unzoo
Version:	4.4
Release:	4
License:	Public Domain
Group:		Applications/Archiving
URL:		ftp://ftp.math.rwth-aachen.de/pub/gap/gap4/util/unzoo.c
Source0:	%{name}.c.gz
# Source0-md5:	a065edbb257c7cf44f97ef69a9467ab2
Patch0:		%{name}-directory_traversal.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unzoo utility is a Public Domain program, distributed with source
code and developed for extracting, testing and viewing the contents of
archives created with the ZOO archiver.

%description -l pl.UTF-8
unzoo jest programem freeware, rozpowszechnianym wraz z kodem
źródłowym, przeznaczonym do rozpakowywania, testowania oraz
przeglądania zawartości archiwów stworzonych przez program ZOO.

%prep
%setup -q -c -T
gzip -dc %{SOURCE0} > unzoo.c
%patch0 -p1

%build
%{__cc} %{rpmcflags} %{rpmldflags} -DSYS_IS_UNIX unzoo.c -o unzoo

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install unzoo $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/unzoo
