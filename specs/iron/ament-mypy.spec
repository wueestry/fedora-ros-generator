# Meta Package
Name:           ros-iron-ament-mypy
Version:        0.14.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ament_mypy and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ament_mypy
Requires:       ros2-iron-ament_mypy-devel

Obsoletes: ros-iron-ament-mypy < 0.14.3-1

%description
Support for mypy static type checking in ament.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.14.3-1
- Update to latest release
