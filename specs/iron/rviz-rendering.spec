# Meta Package
Name:           ros-iron-rviz-rendering
Version:        12.4.7
Release:        1%{?dist}
License:        BSD
URL:            https://github.com/ros2/rviz/blob/ros2/README.md
Summary:        Meta package for ros2-iron-rviz_rendering and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rviz_rendering
Requires:       ros2-iron-rviz_rendering-devel

Obsoletes: ros-iron-rviz-rendering < 12.4.7-1

%description
Library which provides the 3D rendering functionality in rviz.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.12.4.7-1
- Update to latest release
