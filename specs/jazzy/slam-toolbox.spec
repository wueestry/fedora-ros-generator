# Meta Package
Name:           ros-jazzy-slam-toolbox
Version:        2.8.2
Release:        1%{?dist}
License:        LGPL
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-slam_toolbox and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-slam_toolbox
Requires:       ros2-jazzy-slam_toolbox-devel

Obsoletes: ros-jazzy-slam-toolbox < 2.8.2-1

%description
This package provides a sped up improved slam karto with updated SDK
and visualization and modification toolsets

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.8.2-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.8.1-1
- Update to latest release
