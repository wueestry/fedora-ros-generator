# Meta Package
Name:           ros-iron-rviz-ogre-vendor
Version:        12.4.7
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://www.ogre3d.org/
Summary:        Meta package for ros2-iron-rviz_ogre_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rviz_ogre_vendor
Requires:       ros2-iron-rviz_ogre_vendor-devel

Obsoletes: ros-iron-rviz-ogre-vendor < 12.4.7-1

%description
Wrapper around ogre3d, it provides a fixed CMake module and an
ExternalProject build of ogre.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.12.4.7-1
- Update to latest release
