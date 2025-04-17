# Meta Package
Name:           ros-jazzy-steering-controllers-library
Version:        4.23.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://control.ros.org
Summary:        Meta package for ros2-jazzy-steering_controllers_library and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-steering_controllers_library
Requires:       ros2-jazzy-steering_controllers_library-devel

Obsoletes: ros-jazzy-steering-controllers-library < 4.23.0-1

%description
Package for steering robot configurations including odometry and
interfaces.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sun Apr 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.23.0-1
- Update to latest release
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.22.0-1
- Update to latest release
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.21.0-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.18.0-1
- Update to latest release
* Wed Nov 20 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.16.0-1
- Update to latest release
* Tue Oct 15 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.15.0-1
- Update to latest release
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.13.0-1
- Update to latest release
* Wed Jul 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.12.0-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.11.0-1
- Update to latest release
* Wed Jun 05 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.9.0-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.8.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.7.0-1
- Update to latest release
