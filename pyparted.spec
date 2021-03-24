Name:    pyparted
Epoch:   1
Version: 3.11.7
Release: 2
Summary: Python bindings for libparted
License: GPLv2
Group:   System Environment/Libraries
URL:     https://github.com/dcantrell/pyparted
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

%build
PYTHON=python3 %make_build CFLAGS="$RPM_OPT_FLAGS"

%check
PYTHON=python3 make test

%install
PYTHON=python3 %make_install

%files -n python3-pyparted
%doc AUTHORS NEWS README TODO
%license COPYING
%{python3_sitearch}/_ped.*.so
%{python3_sitearch}/parted
%{python3_sitearch}/%{name}-%{version}-*.egg-info

%changelog
* Wed Mar 03 2021 shixuantong <shixuantong@huawei.com> - 3.11.7-2
- add debuginfo and debugsource

* Tue Feb 02 2021 wuchaochao <wuchaochao4@huawei.com> - 3.11.7-1
- Update package version 

* Tue Aug 04 2020 Leo Fang <leofang_94@163.com> - 3.11.6-2
- Update URL of pyparted

* Fri Jul 24 2020 shixuantong <shixuantong@huawei.com> - 3.11.6-1
- update to 3.11.6-1

* Sat Oct 19 2019 openEuler Buildteam <buildteam@openeuler.org> - 1:3.11.0-18
- Package init
