%global debug_package %{nil}

Name:    pyparted
Epoch:   1
Version: 3.11.4
Release: 1
Summary: Python bindings for libparted
License: GPLv2
Group:   System Environment/Libraries
URL:     https://github.com/dcantrell/pyparted

Source0: https://github.com/dcantrell/pyparted/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc git pkgconfig e2fsprogs parted-devel >= 3.2-18

BuildRequires: python3-devel python3-six
BuildRequires: python2-devel python2-six

%description
%{name} is a set of native Python bindings for libparted.  libparted is the
library portion of the GNU parted project.  With pyparted, you can write
applications that interact with disk partition tables and filesystems.

%package -n python2-pyparted
Summary: Python2 bindings for libparted
%{?python_provide:%python_provide python2-pyparted}
Provides: pyparted = %{epoch}:%{version}-%{release}
Provides: pyparted%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes: pyparted < %{epoch}:%{version}-%{release}

%description -n python2-pyparted
Python2 module for libparted.

%package -n python3-pyparted
Summary: Python3 bindings for libparted

%description -n python3-pyparted
Python3 module for libparted.

%prep
%autosetup -n %{name}-%{version} -p1 -Sgit

rm -rf %{py3dir}
mkdir -p %{py3dir}
cp -a . %{py3dir}

%build
PYTHON=python2 %make_build
pushd %{py3dir}
PYTHON=python3 %make_build
popd

%check
PYTHON=python2 make test
pushd %{py3dir}
PYTHON=python3 make test
popd

%install
PYTHON=python2 %make_install
pushd %{py3dir}
PYTHON=python3 %make_install
popd

%files -n python2-pyparted
%doc AUTHORS NEWS README TODO
%license COPYING
%{python2_sitearch}/_ped.so
%{python2_sitearch}/parted
%{python2_sitearch}/%{name}-%{version}-*.egg-info

%files -n python3-pyparted
%doc AUTHORS NEWS README TODO
%license COPYING
%{python3_sitearch}/_ped.*.so
%{python3_sitearch}/parted
%{python3_sitearch}/%{name}-%{version}-*.egg-info

%changelog
* Sat Aug 29 2020 SimpleUpdate Robot <tc@openeuler.org> - 3.11.4-1
- Upgrade to version 3.11.4

* Mon Aug 03 2020 Leo Fang <leofang_94@163.com> - 3.11.2-2
- Update url of Source0 and add yaml file

* Mon Jul 27 2020 Leo Fang <leofang_94@163.com> - 3.11.2-1
- Update to version 3.11.2

* Sat Oct 19 2019 openEuler Buildteam <buildteam@openeuler.org> - 1:3.11.0-18
- Package init
