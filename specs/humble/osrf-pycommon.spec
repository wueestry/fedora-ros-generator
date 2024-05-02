# Meta Package
Name:           ros-humble-osrf-pycommon
Version:        2.0.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-osrf_pycommon and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-osrf_pycommon
Requires:       ros2-humble-osrf_pycommon-devel

Obsoletes: ros-humble-osrf-pycommon < 2.0.2-1

%description
Commonly needed Python modules, used by Python software developed at
OSRF.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.2-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.2-1
- Initial humble build
