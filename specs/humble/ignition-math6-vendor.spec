# Meta Package
Name:           ros-humble-ignition-math6-vendor
Version:        0.0.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/ignitionrobotics/ign-math
Summary:        Meta package for ros2-humble-ignition_math6_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-ignition_math6_vendor
Requires:       ros2-humble-ignition_math6_vendor-devel

Obsoletes: ros-humble-ignition-math6-vendor < 0.0.2-1

%description
This package provides the Ignition Math 6.x library.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.0.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.0.2-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.0.2-1
- Initial humble build
