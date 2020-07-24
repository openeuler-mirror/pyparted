%global debug_package   %{nil}

Name:    pyparted
Epoch:   1
Version: 3.11.6
Release: 1
Summary: Python bindings for libparted
License: GPLv2
Group:   System Environment/Libraries
URL:     https://github.com/rhinstaller/pyparted

Source0: https://github.com/dcantrell/pyparted/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: gcc git pkgconfig e2fsprogs parted-devel >= 3.2-18

BuildRequires: python3-devel python3-six

%description
%{name} is a set of native Python bindings for libparted.  libparted is the
library portion of the GNU parted project.  With pyparted, you can write
applications that interact with disk partition tables and filesystems.

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
pushd %{py3dir}
PYTHON=python3 %make_build
popd

%check
pushd %{py3dir}
PYTHON=python3 make test
popd

%install
pushd %{py3dir}
PYTHON=python3 %make_install
popd

%files -n python3-pyparted
%doc AUTHORS NEWS README TODO
%license COPYING
%{python3_sitearch}/_ped.*.so
%{python3_sitearch}/parted
%{python3_sitearch}/%{name}-%{version}-*.egg-info

%changelog
* Fri Jul 24 2020 shixuantong <shixuantong@huawei.com> - 3.11.6-1
- update to 3.11.6-1

* Sat Oct 19 2019 openEuler Buildteam <buildteam@openeuler.org> - 1:3.11.0-18
- Package init
