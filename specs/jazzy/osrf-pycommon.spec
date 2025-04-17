# Meta Package
Name:           ros-jazzy-osrf-pycommon
Version:        2.1.6
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-osrf_pycommon and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-osrf_pycommon
Requires:       ros2-jazzy-osrf_pycommon-devel

Obsoletes: ros-jazzy-osrf-pycommon < 2.1.6-1

%description
Commonly needed Python modules, used by Python software developed at
OSRF.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Apr 10 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.1.6-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.1.5-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.1.4-1
- Update to latest release
