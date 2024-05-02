# Meta Package
Name:           ros-humble-ament-package
Version:        0.14.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-ament_package and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-ament_package
Requires:       ros2-humble-ament_package-devel

Obsoletes: ros-humble-ament-package < 0.14.0-1

%description
The parser for the manifest files in the ament buildsystem.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.14.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.14.0-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.14.0-1
- Initial humble build
