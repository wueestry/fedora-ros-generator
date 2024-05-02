# Meta Package
Name:           ros-humble-rpyutils
Version:        0.2.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-rpyutils and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rpyutils
Requires:       ros2-humble-rpyutils-devel

Obsoletes: ros-humble-rpyutils < 0.2.1-1

%description
Package containing various utility types and functions for Python

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.2.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.2.1-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.2.1-1
- Initial humble build
