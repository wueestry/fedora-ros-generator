# Meta Package
Name:           ros-jazzy-rviz-ogre-vendor
Version:        14.1.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://www.ogre3d.org/
Summary:        Meta package for ros2-jazzy-rviz_ogre_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rviz_ogre_vendor
Requires:       ros2-jazzy-rviz_ogre_vendor-devel

Obsoletes: ros-jazzy-rviz-ogre-vendor < 14.1.0-1

%description
Wrapper around ogre3d, it provides a fixed CMake module and an
ExternalProject build of ogre.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.0-1
- Update to latest release
