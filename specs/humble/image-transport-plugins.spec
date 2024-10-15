# Meta Package
Name:           ros-humble-image-transport-plugins
Version:        2.5.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/image_transport_plugins
Summary:        Meta package for ros2-humble-image_transport_plugins and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-image_transport_plugins
Requires:       ros2-humble-image_transport_plugins-devel

Obsoletes: ros-humble-image-transport-plugins < 2.5.2-1

%description
A set of plugins for publishing and subscribing to sensor_msgs/Image
topics in representations other than raw pixel data. For example, for
viewing a stream of images off-robot, a video codec will give much
lower bandwidth and latency. For low frame rate tranport of high-
definition images, you might prefer sending them as JPEG or PNG-
compressed form.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.2-1
- Update to latest release
