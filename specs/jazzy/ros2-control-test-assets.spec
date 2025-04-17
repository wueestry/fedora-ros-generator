# Meta Package
Name:           ros-jazzy-ros2-control-test-assets
Version:        4.28.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ros2_control_test_assets and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ros2_control_test_assets
Requires:       ros2-jazzy-ros2_control_test_assets-devel

Obsoletes: ros-jazzy-ros2-control-test-assets < 4.28.0-1

%description
Shared test resources for ros2_control stack

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sun Apr 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.28.0-1
- Update to latest release
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.27.0-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.23.0-1
- Update to latest release
* Wed Nov 20 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.20.0-1
- Update to latest release
* Tue Oct 15 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.18.0-1
- Update to latest release
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.16.1-1
- Update to latest release
* Wed Jul 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.14.0-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.13.0-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.11.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.8.0-1
- Update to latest release
