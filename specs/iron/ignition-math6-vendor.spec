# Meta Package
Name:           ros-iron-ignition-math6-vendor
Version:        0.1.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/ignitionrobotics/ign-math
Summary:        Meta package for ros2-iron-ignition_math6_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ignition_math6_vendor
Requires:       ros2-iron-ignition_math6_vendor-devel

Obsoletes: ros-iron-ignition-math6-vendor < 0.1.0-1

%description
This package provides the Ignition Math 6.x library.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.1.0-1
- Update to latest release
