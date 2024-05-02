# Meta Package
Name:           ros-humble-ignition-cmake2-vendor
Version:        0.0.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/ignitionrobotics/ign-cmake
Summary:        Meta package for ros2-humble-ignition_cmake2_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-ignition_cmake2_vendor
Requires:       ros2-humble-ignition_cmake2_vendor-devel

Obsoletes: ros-humble-ignition-cmake2-vendor < 0.0.2-1

%description
This package provides the Ignition CMake 2.x library.

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
