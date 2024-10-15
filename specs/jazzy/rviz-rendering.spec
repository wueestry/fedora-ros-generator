# Meta Package
Name:           ros-jazzy-rviz-rendering
Version:        14.1.4
Release:        1%{?dist}
License:        BSD
URL:            https://github.com/ros2/rviz/blob/ros2/README.md
Summary:        Meta package for ros2-jazzy-rviz_rendering and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rviz_rendering
Requires:       ros2-jazzy-rviz_rendering-devel

Obsoletes: ros-jazzy-rviz-rendering < 14.1.4-1

%description
Library which provides the 3D rendering functionality in rviz.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.4-1
- Update to latest release
* Wed Jul 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.3-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.2-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.0-1
- Update to latest release
