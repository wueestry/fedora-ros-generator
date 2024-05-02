# Meta Package
Name:           ros-iron-osrf-pycommon
Version:        2.1.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-osrf_pycommon and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-osrf_pycommon
Requires:       ros2-iron-osrf_pycommon-devel

Obsoletes: ros-iron-osrf-pycommon < 2.1.2-1

%description
Commonly needed Python modules, used by Python software developed at
OSRF.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.1.2-1
- Update to latest release
